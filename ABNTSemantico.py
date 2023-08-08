from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from typing import List


class ABNTSemantico(ABNTVisitor):
    
    def visitPrograma(self, ctx: ABNTParser.ProgramaContext):
        return super().visitPrograma(ctx)