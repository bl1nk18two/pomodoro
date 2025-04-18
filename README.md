# pomodoro

![GitHub](https://img.shields.io/github/license/bl1nk18two/tempo_pypack)
[![Status: Em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)]()

Um temporizador Pomodoro simples que roda no terminal e envia notificações no Windows para avisar sobre os ciclos de trabalho, intervalo curto e descanso longo.

## Como Usar

Execute o script Python no terminal com os seguintes argumentos:

  ```bash
  python pomodoro.py -t 25 -i 5 -d 15 -qp 4
  ```

### Apresentação de Uso
![Pomodoro rodando](https://github.com/user-attachments/assets/c1ce840d-5012-485f-8082-d39505720e4b)
![Notificação](https://github.com/user-attachments/assets/cd6e9eba-0c6e-4106-b55e-2ecab213be06)


### ⌨️ Argumentos disponíveis:

| Curto | Longo                   | Descrição                                                 |
|-------|-------------------------|-----------------------------------------------------------|
| `-t`  | `--trabalho`            | Tempo (em minutos) de cada ciclo de trabalho             |
| `-i`  | `--intervalo`           | Tempo (em minutos) dos intervalos curtos entre pomodoros |
| `-d`  | `--descanso`            | Tempo (em minutos) do descanso longo após os ciclos      |
| `-qp` | `--quantidade_pomodoros`| Número de pomodoros antes do descanso longo              |


## 📦 Requisitos
Python 3.x

Biblioteca win11toast (para as notificações no Windows)

Instalação da dependência:
 ```bash
  pip install win11toast
  ```


## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.


