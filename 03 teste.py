import tkinter as tk
from tkinter import ttk, messagebox
from collections import Counter
import math

# --- Funções de Lógica de Probabilidade ---

def calculate_item_probabilities(items_str):
    """Calcula a probabilidade de cada item único em uma lista de strings."""
    if not items_str.strip():
        return "Por favor, insira alguns itens."

    items = [item.strip() for item in items_str.split(',')]
    if not items:
        return "Nenhum item válido encontrado após separar por vírgula."

    total_items = len(items)
    item_counts = Counter(items)
    
    results = f"Total de itens: {total_items}\n\nProbabilidades:\n"
    for item, count in item_counts.items():
        probability = count / total_items
        results += f"  P({item}): {count}/{total_items} = {probability:.4f} (ou {probability*100:.2f}%)\n"
    return results

def factorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    return math.factorial(n)

def permutations(n, r):
    """Calcula nPr = n! / (n-r)!"""
    if r > n:
        raise ValueError("r não pode ser maior que n para permutações.")
    if n < 0 or r < 0:
        raise ValueError("n e r devem ser não-negativos.")
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    """Calcula nCr = n! / (r! * (n-r)!)"""
    if r > n:
        raise ValueError("r não pode ser maior que n para combinações.")
    if n < 0 or r < 0:
        raise ValueError("n e r devem ser não-negativos.")
    return factorial(n) // (factorial(r) * factorial(n - r))

# --- Funções da Interface Gráfica (GUI) ---

def on_calculate_item_prob():
    items_input = entry_items.get()
    result_text = calculate_item_probabilities(items_input)
    text_results.delete(1.0, tk.END)
    text_results.insert(tk.END, result_text)

def on_calculate_p_c():
    try:
        n_val = int(entry_n.get())
        r_val = int(entry_r.get())

        result_p_c = "Resultados de Permutação e Combinação:\n"
        
        try:
            perm = permutations(n_val, r_val)
            result_p_c += f"  Permutações P({n_val}, {r_val}): {perm}\n"
        except ValueError as e:
            result_p_c += f"  Erro na Permutação: {e}\n"

        try:
            comb = combinations(n_val, r_val)
            result_p_c += f"  Combinações C({n_val}, {r_val}): {comb}\n"
        except ValueError as e:
            result_p_c += f"  Erro na Combinação: {e}\n"
            
        text_results.delete(1.0, tk.END)
        text_results.insert(tk.END, result_p_c)

    except ValueError:
        messagebox.showerror("Erro de Entrada", "N e R devem ser números inteiros.")
    except Exception as e:
        messagebox.showerror("Erro Inesperado", str(e))


# --- Configuração da Janela Principal ---
root = tk.Tk()
root.title("Calculadora de Probabilidades Simples")
root.geometry("550x500")

# Estilo (opcional, mas melhora a aparência)
style = ttk.Style()
style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'

# Frame para probabilidades de itens
frame_items = ttk.LabelFrame(root, text="Probabilidade de Itens na Lista", padding=(10, 5))
frame_items.pack(padx=10, pady=10, fill="x")

ttk.Label(frame_items, text="Insira os itens separados por vírgula (ex: 1,2,2,cara,coroa):").pack(pady=5, anchor="w")
entry_items = ttk.Entry(frame_items, width=60)
entry_items.pack(pady=5, fill="x")
ttk.Button(frame_items, text="Calcular Probabilidade dos Itens", command=on_calculate_item_prob).pack(pady=5)

# Frame para Permutações e Combinações
frame_pc = ttk.LabelFrame(root, text="Permutações e Combinações", padding=(10, 5))
frame_pc.pack(padx=10, pady=10, fill="x")

sub_frame_pc_inputs = ttk.Frame(frame_pc)
sub_frame_pc_inputs.pack(fill="x")

ttk.Label(sub_frame_pc_inputs, text="Valor de n:").pack(side=tk.LEFT, padx=5)
entry_n = ttk.Entry(sub_frame_pc_inputs, width=10)
entry_n.pack(side=tk.LEFT, padx=5)

ttk.Label(sub_frame_pc_inputs, text="Valor de r:").pack(side=tk.LEFT, padx=5)
entry_r = ttk.Entry(sub_frame_pc_inputs, width=10)
entry_r.pack(side=tk.LEFT, padx=5)

ttk.Button(frame_pc, text="Calcular Permutações e Combinações", command=on_calculate_p_c).pack(pady=10)


# Área de Resultados
frame_results = ttk.LabelFrame(root, text="Resultados", padding=(10,5))
frame_results.pack(padx=10, pady=10, fill="both", expand=True)

text_results = tk.Text(frame_results, wrap=tk.WORD, height=10, width=60)
text_results.pack(fill="both", expand=True, pady=5)
scrollbar = ttk.Scrollbar(text_results, command=text_results.yview)
text_results['yscrollcommand'] = scrollbar.set
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # Descomente se quiser a scrollbar visível sempre

# Iniciar a interface
root.mainloop()