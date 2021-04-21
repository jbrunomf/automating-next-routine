# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import time
import subprocess
import psutil


EXE_PATH = 'C:\\Next\\AgendamentoNext\\Next_Agendamento.exe'
PROCESS_NAME = 'Next_Agendamento.exe'


def check_if_popen(pname):
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
    try:
        subprocess.Popen(EXE_PATH)
        time.sleep(10)
        check_options()
    except OSError as err:
        print(err)


def check_options():
    """
    Procura pelo conteúdo da imagem 'check.png', e clica na área indicada (imagem).
    Caso a imagem não seja encontrada, retorna ImageNotFoundException.
    :return:
    """
    try:
        turn_on_label_img = pyautogui.locateOnScreen('check.png')
        pyautogui.click(turn_on_label_img)
        time.sleep(2)
        turn_on_label_img = pyautogui.locateOnScreen('check.png')
        # Marcar opção buscar agendamento
        pyautogui.click(turn_on_label_img)
        time.sleep(2)
    except pyautogui.ImageNotFoundException as e:
        print(str(e))
    minimize()


def minimize():
    """
    Minimiza a janela do app Agendamento.exe. (windows api call)
    :return:
    """
    try:
        window_list = pyautogui.getWindowsWithTitle('Next - Agendamento')
        for window in window_list:
            if window.title == 'Next - Agendamento':
                window.minimize()
    except Exception as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_if_popen(PROCESS_NAME)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
