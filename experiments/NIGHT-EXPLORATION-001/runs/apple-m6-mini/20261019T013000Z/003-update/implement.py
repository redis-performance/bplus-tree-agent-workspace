#!/usr/bin/env python3
import difflib,hashlib,json,shutil,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent;REL=OUT.relative_to(ROOT)
BASE=Path('scratch/m6-update/variants');BASE.mkdir(exist_ok=True)
source=Path('src/zset_btree.c').read_text()
# All variants change only the response to an exact packing failure, after both order checks.
start=source.index('static int zbtScoreUpdateInPlace(');end=source.index('/* Record the page share',start)
function=source[start:end];needle='    if (!zbtScoreLeafPackScore(leaf, score, &delta)) return 0;';assert function.count(needle)==1
common='''/* Re-encode scores without moving member records or changing a leaf ID.
 * Return zero before writing when the changed arrays do not fit. */
static int zbtScoreUpdateReencode(zbtScoreLeaf *leaf, unsigned int pos,
                                  double score)
{
    unsigned int count = leaf->n.count;
    double scores[ZBT_SCORE_LEAF_MAX];
    for (unsigned int i = 0; i < count; i++)
        scores[i] = i == pos ? score : zbtScoreLeafScore(leaf, i);
    uint64_t base;
    uint8_t width, shift;
ENCODING
    size_t score_bytes = zbtScoreLeafScoreBytes(count, width);
    size_t index_end = offsetof(zbtScoreLeaf, data) + score_bytes +
                       count * (sizeof(uint16_t) + sizeof(uint8_t));
    if (index_end > leaf->record_start) return 0;
SAVE_METADATA
    leaf->score_base = base;
    leaf->score_bits = width;
    leaf->n.score_shift = shift;
    memset(leaf->data, 0, score_bytes);
RESTORE_METADATA
    for (unsigned int i = 0; i < count; i++) {
        zbtScoreLeafWriteScore(leaf, i, scores[i]);
        debugServerAssert(zbtScoreLeafScore(leaf, i) == scores[i]);
    }
    return 1;
}

'''
minimal='    zbtScoreEncoding(count, scores, leaf->reversed, &base, &width, &shift);'
enc_c='''    /* Preserve the existing base and all values representable before.
     * This conservative envelope can fall back even when minimal packing fits. */
    uint64_t ordered = zbtScoreToOrdered(score);
    base = leaf->score_base;
    if ((!leaf->reversed && ordered < base) ||
        (leaf->reversed && ordered > base)) return 0;
    uint64_t distance = leaf->reversed ? base - ordered : ordered - base;
    shift = leaf->n.score_shift;
    if (distance && (unsigned int)__builtin_ctzll(distance) < shift)
        shift = __builtin_ctzll(distance);
    unsigned int old_width = leaf->score_bits ?
        leaf->score_bits + leaf->n.score_shift - shift : 0;
    unsigned int new_width = zbtBitsNeeded(distance >> shift);
    if (old_width > 64) return 0;
    width = old_width > new_width ? old_width : new_width;'''
save_a='''    uint16_t locations[ZBT_SCORE_LEAF_MAX];
    uint8_t tags[ZBT_SCORE_LEAF_MAX];
    for (unsigned int i = 0; i < count; i++) {
        locations[i] = zbtScoreLeafOffset(leaf, i);
        tags[i] = zbtScoreLeafTag(leaf, i);
    }'''
restore_a='''    uint16_t *offsets = zbtScoreLeafOffsets(leaf);
    uint8_t *hash_tags = zbtScoreLeafHashTags(leaf);
    for (unsigned int i = 0; i < count; i++) {
        unsigned int physical = zbtScoreLeafPhysicalPos(leaf, i);
        offsets[physical] = locations[i];
        hash_tags[physical] = tags[i];
    }'''
save_b='''    size_t old_score_bytes = zbtScoreLeafScoreBytes(count, leaf->score_bits);
    memmove(leaf->data + score_bytes, leaf->data + old_score_bytes,
            count * (sizeof(uint16_t) + sizeof(uint8_t)));'''
choices={'A':(minimal,save_a,restore_a),'B':(minimal,save_b,''),'C':(enc_c,save_b,'')}
m={'created_utc':datetime.now(timezone.utc).isoformat(),'population':'three sequential implementations by one worker; not independent agents','backend':'Codex/GPT-6 family; exact serving model/token costs unknown','source_commit':'33bf7899','chair_commit':'f8d2badf','isolation':'Git worktree creation denied once (.git/worktrees/base Operation not permitted); separate copied source/build directories, no retry','variants':{}}
for variant in ('0','A','B','C'):
 folder=BASE/variant;assert not folder.exists();folder.mkdir()
 for name in ('src','compat','vendor','tests','bench'):shutil.copytree(name,folder/name)
 shutil.copy2('Makefile',folder/'Makefile')
 (folder/REL).mkdir(parents=True)
 for f in ('update-path-bench.c','semantic-check.c'):shutil.copy2(OUT/f,folder/REL/f)
 (folder/REL/'../002-rank').mkdir(exist_ok=True);shutil.copy2(OUT/'../002-rank/night-rank-sampler.h',folder/REL/'../002-rank/night-rank-sampler.h')
 if variant!='0':
  encoding,save,restore=choices[variant];helper=common.replace('ENCODING',encoding).replace('SAVE_METADATA',save).replace('RESTORE_METADATA',restore)
  replacement='''    if (!zbtScoreLeafPackScore(leaf, score, &delta)) {
        if (!zbtScoreUpdateReencode(leaf, pos, score)) return 0;
        if (pos + 1 == leaf->n.count) zbtScoreUpdatePath(&leaf->n, 0);
        return 1;
    }'''
  changed=source[:start]+helper+function.replace(needle,replacement)+source[end:]
  (folder/'src/zset_btree.c').write_text(changed)
  public=OUT/'variants'/variant;public.mkdir(parents=True)
  (public/'candidate.patch').write_text(''.join(difflib.unified_diff(source.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  (public/'implementation.md').write_text(f'# Sequential implementation {variant}\n\nHypothesis M6-UPDATE-REPACK-001; baseline33bf7899; chairf8d2badf.\n'+{'A':'Minimal encoding, logical offset/tag snapshots and explicit physical restoration.','B':'Minimal encoding, physical contiguous offset/tag memmove before score rewrite.','C':'Keep base, loosen shift/widen field envelope; physical metadata memmove. Conservative fallback for base/headroom/width constraints.'}[variant]+'\nNo added allocations, fields or member-record writes. No change before order checks. Exact finite scores, reversed mapping and zero-width/64-bit packing require validation. No independent implementation agent. Exact model/cost unknown.\n')
  m['variants'][variant]={'source_sha256':hashlib.sha256(changed.encode()).hexdigest(),'patch_sha256':hashlib.sha256((public/'candidate.patch').read_bytes()).hexdigest()}
 else:m['variants'][variant]={'source_sha256':hashlib.sha256(source.encode()).hexdigest()}
 m['variants'][variant]['snapshot']=str(folder)
 m['variants'][variant]['referee_hashes']={str(f.relative_to(folder)):hashlib.sha256(f.read_bytes()).hexdigest() for f in folder.rglob('*') if f.is_file() and not str(f.relative_to(folder)).startswith('src/zset_btree.c')}
(OUT/'implementation-manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print('3 isolated patches and 4 snapshots created')
