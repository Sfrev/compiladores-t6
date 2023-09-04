class ABNTSemanticoUtils:

    errosSemanticos = []

    @staticmethod
    def adicionarErroSemantico(token, mensagem):

        linha = token.line
        
        ABNTSemanticoUtils.errosSemanticos.append(f"Linha {linha}: {mensagem}")