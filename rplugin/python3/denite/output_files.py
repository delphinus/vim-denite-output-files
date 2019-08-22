from denite.source.output import Source as Base
from denite.util import Nvim


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.name = "output_files"
        self.kind = "file"
