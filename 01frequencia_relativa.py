import tkinter as tk
from tkinter import messagebox
import random

def frequencia_relativa(evento, espaco_amostral, n_simulacoes=10000):
    """
    Calcula a frequência relativa (probabilidade experimental) de um evento usando simulação de Monte Carlo.

    Parâmetros:
    evento -- função que recebe um resultado do espaço amostral e retorna True se o evento ocorreu
    espaco_amostral -- lista ou função que gera os possíveis resultados
    n_simulacoes -- número de simulações a serem realizadas (padrão: 10.000)

    Retorno:
    probabilidade -- valor entre 0 e 1 representando a frequência relativa do evento
    """
    ocorrencias = 0
    for _ in range(n_simulacoes):
        if callable(espaco_amostral):
            resultado = espaco_amostral()
        else:
            resultado = random.choice(espaco_amostral)
        if evento(resultado):
            ocorrencias += 1
    probabilidade = ocorrencias / n_simulacoes
    return probabilidade

def calcular_probabilidade():
    try:
        # Lê o espaço amostral da entrada (ex: 1,2,3,4,5,6)
        espaco = [int(x.strip()) for x in entrada_espaco.get().split(',')]
        # Lê o valor do evento (ex: "par" ou um número específico)
        evento_valor = entrada_evento.get().strip().lower()
        # Define a função do evento
        if evento_valor == "par":
            evento = lambda x: x % 2 == 0
        elif evento_valor == "impar":
            evento = lambda x: x % 2 != 0
        else:
            valor = int(evento_valor)
            evento = lambda x: x == valor
        # Calcula a probabilidade
        prob = frequencia_relativa(evento, espaco)
        messagebox.showinfo("Resultado", f"Probabilidade estimada: {prob:.4f}")
    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Calculadora de Probabilidade Experimental")

# Espaço amostral
tk.Label(root, text="Espaço amostral (ex: 1,2,3,4,5,6):").pack(pady=2)
entrada_espaco = tk.Entry(root, width=30)
entrada_espaco.pack(pady=2)

# Evento
tk.Label(root, text="Evento (ex: par, impar ou valor exato):").pack(pady=2)
entrada_evento = tk.Entry(root, width=30)
entrada_evento.pack(pady=2)

# Botão para calcular
btn = tk.Button(root, text="Calcular Probabilidade", command=calcular_probabilidade)
btn.pack(pady=10)

root.mainloop()