""" 
Comandos:
-t [argumento]| --trabalho [argumento] = trabalho
-i [argumento]| --intervalo [argumento] = intervalo
-d [argumento]| --descanso [argumento] = descanso
-qp [argumento]| --quantidade_pomodoros [argumento] = quantidade de pomodoros
"""

import sys

from src import retorna_argumentos, GerenciaPomodoro

def main():
    try:
        trabalho, intervalo, descanso, quantidade_pomodoros = retorna_argumentos()

        GerenciaPomodoro(trabalho=trabalho,
                        intervalo=intervalo,
                        descanso=descanso,
                        quantidade_pomodoros=quantidade_pomodoros
                        )

    except KeyboardInterrupt:
        print("\n⏹️  Pomodoro Encerrado. Até a Próxima...")
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
