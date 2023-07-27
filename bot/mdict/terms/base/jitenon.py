from bot.mdict.terms.base.terminator import BaseTerminator


class JitenonTerminator(BaseTerminator):
    def __init__(self, target):
        super().__init__(target)
        self._glossary_maker = None

    def _glossary(self, entry):
        if entry.entry_id in self._glossary_cache:
            return self._glossary_cache[entry.entry_id]
        glossary = self._glossary_maker.make_glossary(entry, self._media_dir)
        self._glossary_cache[entry.entry_id] = glossary
        return glossary

    def _link_glossary_parameters(self, entry):
        return []

    def _subentry_lists(self, entry):
        return []
