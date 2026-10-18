# Linked-code isolation audit

All C inputs match HARNESS-004. All assembler bytes outside the two inserted padding
directives round-trip exactly, including binary test literals. All named symbols keep
their addresses except zbtreeIteratorNext, which moves by the specified offset. Caller
address and relocation-normalized instructions match; iterator instructions/relative
control flow match. Direct-call displacement encodings necessarily follow the moved
callee. This is not an assertion that every binary byte is identical. Padding is outside
function entry/return paths. No cache or predictor mechanism established.

[
  {
    "pad": 0,
    "iterator_address": "0x10000b65c",
    "mod64": 28,
    "caller_address": "0x1000036bc",
    "only_symbol_moved": {},
    "caller_instructions": 274,
    "iterator_instructions": 155
  },
  {
    "pad": 16,
    "iterator_address": "0x10000b66c",
    "mod64": 44,
    "caller_address": "0x1000036bc",
    "only_symbol_moved": {
      "_zbtreeIteratorNext": 16
    },
    "caller_instructions": 274,
    "iterator_instructions": 155
  },
  {
    "pad": 32,
    "iterator_address": "0x10000b67c",
    "mod64": 60,
    "caller_address": "0x1000036bc",
    "only_symbol_moved": {
      "_zbtreeIteratorNext": 32
    },
    "caller_instructions": 274,
    "iterator_instructions": 155
  },
  {
    "pad": 48,
    "iterator_address": "0x10000b68c",
    "mod64": 12,
    "caller_address": "0x1000036bc",
    "only_symbol_moved": {
      "_zbtreeIteratorNext": 48
    },
    "caller_instructions": 274,
    "iterator_instructions": 155
  }
]
