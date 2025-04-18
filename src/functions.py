import argparse
import os

def retorna_argumentos():
    """ Retorna os argumentos inseridos no terminal """

    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument("-t", "--trabalho", type=int, default=25, help="Tempo de trabalho (minutos)")
    parser.add_argument("-i", "--intervalo", type=int, default=5, help="Tempo de intervalo curto (minutos)")
    parser.add_argument("-d", "--descanso", type=int, default=15, help="Tempo de descanso longo (minutos)")
    parser.add_argument("-qp", "--quantidade_pomodoros", type=int, default=4, help="Quantidade de pomodoros até o descanso.")


    args = parser.parse_args()
    if args.quantidade_pomodoros < 2:
        raise ValueError("O argumeto '-qp' deve ser igual ou maior que '2'")
    return args.trabalho, args.intervalo, args.descanso, args.quantidade_pomodoros


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
