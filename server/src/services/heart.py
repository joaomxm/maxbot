import subprocess,os
from ..utils.RobotLed.robot import Robot
from dotenv import load_dotenv

load_dotenv()
PATH_SCRIPT_ACTIONS = os.getenv("PATH_SCRIPT_ACTIONS")

nome_acao = {'nome':None}
processos = []

def executar(acao:str):
    """
    Funcao que inicia o script do LED

    Args:
        acao (str): comando que corresponde a uma face existente

 """
    robo = Robot()

    if nome_acao['nome'] == acao:
        robo.clean()
        limpar_processos()
        nome_acao['nome'] = None
        print('Processo excluido!')
    else:
        robo.clean()
        limpar_processos()
        print('Processo excluido!')

        processo = subprocess.Popen(["python3",PATH_SCRIPT_ACTIONS,acao])
        processos.append(processo)
        nome_acao['nome'] = acao
        print(f'Novo processo: {acao}')    
    

def limpar_processos():
    if len(processos) > 0:
        for processo in processos:
            processo.kill()
        processos.clear()