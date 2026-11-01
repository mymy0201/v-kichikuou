# Demo guide

Machine-readable pair rules can live beside normal Markdown prose:

```pronouns
[
  {"speaker":"Aster", "addressee":"Mira", "self":"ta", "call":"cô", "context":"Ordinary conversation"},
  {"speaker":"Mira", "addressee":"Aster", "self":"tôi", "call":"anh", "context":"Ordinary conversation"}
]
```

The editor uses exact character-name pairs. Mark ambiguous occurrences such as
"cô" and "anh" as Call before applying. Third-person references remain separate.
