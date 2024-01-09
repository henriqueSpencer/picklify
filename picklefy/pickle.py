import pickle
import os
import inspect

class PickleService:
    """
    Classe para acelerar a utilização da serialização
    by: Henrique Spencer Albuquerque
    """
    def init(self):
        arq = os.path.abspath(inspect.getfile(self.__class__))
        self.diretorio_atual = os.path.join(os.path.dirname(arq), 'pickle_files')
        #self.diretorio_atual = os.path.dirname(arq)

    def serialize(self, file_name: str, variavel=None):
        """

        @param file_name: é o nome do arquivo que voce quer salvar ou quer pegar
        @param variavel: é o conteudo que deve ser salvo, caso não seja passado nada quer dizer q voce esta apenas buscando um arquivo
        @return:
        """
        try:
            acao = 'wb'
            if variavel is None:
                acao = 'rb'
            file_name_complete = f'{file_name}.pkl'
            arquivo = os.path.join(self.diretorio_atual, file_name_complete)

            with open(arquivo, acao) as file:
                if acao == 'wb':
                    pickle.dump(variavel, file)
                    return True
                else:
                    variavel = pickle.load(file)
                    return variavel
        except Exception as e:
            print(e)
            return False

if name == '__main__':
    df_test = 'sfgg sdff'
    import pandas as pd
    PickleService().serialize(file_name='df_testt', variavel=df_test)
    # PickleService().serialize(df_relatorio1, 'df_relatorio1', acao='wb', file_version='_v1')
    # df_relatorio1 = PickleService().serialize('', 'df_relatorio1', acao='rb', file_version='_v1')

