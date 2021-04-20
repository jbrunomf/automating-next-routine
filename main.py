# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import time
import subprocess
import psutil

EXE_PATH = 'C:\\Next\\AgendamentoNext\\Next_Agendamento.exe'
PROCESS_NAME = 'Next_Agendamento.exe'


def verify_if_popen(pname):
    """
    Verifica se existe algum processo ativo cujo o attr name seja == ao parâmetro pname.
    Caso exista, o processo será finalizado.
    :param pname:
    :return:
    """
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.name() == pname:
                process.kill()
                time.sleep(2)
    except Exception as e:
        print(str(e))
    start_process()


def start_process():
    """
    Exibe mensagem de alerta, indicando o início do processo.
    :return:
    """
    # pyautogui.alert('Iniciando rotina - Next Agendamento. Pressione OK para continuar o processo.\nNão faça uso da máquina até que a mensagem de sucesso'
    #                 'Seja exibida!')
    # time.sleep(1)
    subprocess.Popen(EXE_PATH)
    time.sleep(10)
    check_options()


def check_options():
    """
    Procura pelo conteúdo da imagem 'ligado.png', e clica na área indicada.
    Caso a imagem não seja encontrada, retorna ImageNotFoundException.
    :return:
    """
    try:
        turn_on_label_img = pyautogui.locateOnScreen('img/ligado.png')
        pyautogui.click(turn_on_label_img)
        time.sleep(2)
        turn_on_label_img = pyautogui.locateOnScreen('img/ligado.png')
        # Marcar opção buscar agendamento
        pyautogui.click(turn_on_label_img)
        time.sleep(2)
        # Minimizar App
        pyautogui.click(1103, 427)
        time.sleep(2)
    except Exception as e:
        print(str(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify_if_popen(PROCESS_NAME)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
