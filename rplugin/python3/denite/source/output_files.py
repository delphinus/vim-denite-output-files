from denite.source.output import Source as Base
from denite.util import Nvim, UserContext, Candidates, abspath


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = "output_files"
        self.kind = "file"
        self.default_action = "open"

    def gather_candidates(self, context: UserContext) -> Candidates:
        return [
            {"word": x["word"], "action__path": abspath(self.vim, x["word"])}
            for x in super().gather_candidates(context)
        ]
