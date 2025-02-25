from bot.mdict.terms.base.terminator import BaseTerminator
from bot.mdict.glossary.smk8 import make_glossary


class Terminator(BaseTerminator):
    def _glossary(self, entry):
        if entry.entry_id in self._glossary_cache:
            return self._glossary_cache[entry.entry_id]
        glossary = make_glossary(entry, self._media_dir)
        self._glossary_cache[entry.entry_id] = glossary
        return glossary

    def _link_glossary_parameters(self, entry):
        return [
            [entry.children, "子項目"],
            [entry.phrases, "句項目"],
        ]

    def _subentry_lists(self, entry):
        return [
            entry.children,
            entry.phrases,
            entry.kanjis,
        ]
