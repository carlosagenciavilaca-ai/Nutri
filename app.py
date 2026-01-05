
import streamlit as st

# Configuração da Página
st.set_page_config(page_title="NutriEvo Pro - IA Nutricional", layout="wide")

# Estilo CSS para melhorar a aparência
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .diet-card { background-color: #e1f5fe; padding: 20px; border-radius: 10px; border-left: 5px solid #0288d1; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍎 NutriEvo Pro")
st.subheader("O Próximo Nível da sua Evolução Física")

# --- SIDEBAR: INPUT DE DADOS ---
with st.sidebar:
    st.header("Seus Dados")
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
    idade = st.number_input("Idade", 15, 90, 30)
    peso = st.number_input("Peso (kg)", 40.0, 200.0, 70.0)
    altura = st.number_input("Altura (cm)", 120, 220, 175)
    
    objetivo = st.selectbox("Objetivo", [
        "Cutting (Perda de Gordura)", 
        "Manutenção", 
        "Bulking (Ganho de Massa)"
    ])
    
    atividade = st.select_slider("Nível de Atividade", 
        options=["Sedentário", "Leve", "Moderado", "Intenso", "Atleta"])

# --- LÓGICA CIENTÍFICA ---
def calcular_macros(genero, peso, altura, idade, objetivo, atividade):
    # 1. TMB (Mifflin-St Jeor)
    if genero == "Masculino":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    
    # 2. Fator de Atividade
    fatores = {"Sedentário": 1.2, "Leve": 1.375, "Moderado": 1.55, "Intenso": 1.725, "Atleta": 1.9}
    tdee = tmb * fatores[atividade]
    
    # 3. Ajuste por Objetivo e Estratégias Científicas
    if "Cutting" in objetivo:
        calorias_alvo = tdee * 0.80  # Déficit de 20% para preservar metabolismo
        prot = peso * 2.2  # Proteína alta para saciedade e músculo
        gord = peso * 0.7
    elif "Bulking" in objetivo:
        calorias_alvo = tdee + 300   # Superávit leve para ganho limpo
        prot = peso * 1.8
        gord = peso * 0.9
    else:
        calorias_alvo = tdee
        prot = peso * 2.0
        gord = peso * 0.8
        
    carbs = (calorias_alvo - (prot * 4) - (gord * 9)) / 4
    return round(calorias_alvo), round(prot), round(carbs), round(gord)

cals, p, c, g = calcular_macros(genero, peso, altura, idade, objetivo, atividade)

# --- DISPLAY DE RESULTADOS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Calorias Diárias", f"{cals} kcal")
col2.metric("Proteínas", f"{p}g")
col3.metric("Carboidratos", f"{c}g")
col4.metric("Gorduras", f"{g}g")

st.divider()

# --- ESTRATÉGIAS CIENTÍFICAS ---
st.header("🚀 Estratégias para Acelerar seu Resultado")
expander = st.expander("Clique para ver suas dicas personalizadas")
if "Cutting" in objetivo:
    expander.write("""
    - **Densidade Calórica:** Troque arroz branco por batata ou vegetais para maior volume com menos calorias.
    - **Termogênese:** Aumente o consumo de cafeína e chá verde (estudos mostram aumento de 3-4% no gasto calórico).
    - **Refeição Pré-Treino:** Foque em 30g de carboidratos complexos para manter a performance mesmo em déficit.
    """)
else:
    expander.write("""
    - **Superávit Progressivo:** Não suba as calorias de uma vez para evitar ganho de gordura excessivo.
    - **Timing de Proteína:** Distribua sua proteína em 4-5 refeições para maximizar a síntese proteica (MPS).
    - **Carboidratos:** Consuma 50% dos seus carboidratos no período de 3h antes e 3h depois do treino.
    """)

# --- CALCULADORA DE SUBSTITUIÇÃO INTELIGENTE ---
st.header("🔄 Calculadora de Substituição")
st.info("Quer trocar um alimento? Eu calculo a quantidade exata para manter seus macros!")

col_sub1, col_sub2, col_sub3 = st.columns(3)

with col_sub1:
    alimento_original = st.selectbox("Alimento que quer tirar", ["Arroz Branco", "Frango Grelhado", "Ovo Cozido", "Pão de Forma"])
    gramas_original = st.number_input("Quantidade original (g)", 10, 500, 100)

with col_sub2:
    alimento_novo = st.selectbox("Alimento que quer incluir", ["Batata Doce", "Patinho Moído", "Tilápia", "Abacate"])

# Banco de dados simples para exemplo (Pode ser expandido com API)
db = {
    "Arroz Branco": 1.3, "Frango Grelhado": 1.65, "Ovo Cozido": 1.55, "Pão de Forma": 2.5,
    "Batata Doce": 0.86, "Patinho Moído": 2.19, "Tilápia": 0.96, "Abacate": 1.6
}

if st.button("Calcular Substituição"):
    cal_orig = gramas_original * db[alimento_original]
    nova_qtd = cal_orig / db[alimento_novo]
    st.success(f"Para manter as calorias, substitua {gramas_original}g de {alimento_original} por **{nova_qtd:.0f}g** de {alimento_novo}.")

# --- SUGESTÃO DE DIETA BASEADA EM IA ---
st.header("📋 Exemplo de Estrutura de Dieta")
st.markdown(f"""
<div class="diet-card">
    <b>Café da Manhã:</b> {p*0.25:.0f}g Prot | {c*0.2:.0f}g Carbo<br>
    <b>Almoço:</b> {p*0.25:.0f}g Prot | {c*0.3:.0f}g Carbo<br>
    <b>Lanche:</b> {p*0.2:.0f}g Prot | {c*0.2:.0f}g Carbo<br>
    <b>Jantar:</b> {p*0.3:.0f}g Prot | {c*0.3:.0f}g Carbo
</div>
""", unsafe_allow_html=True)

st.caption("Nota: Este app utiliza as fórmulas de Mifflin-St Jeor e diretrizes da ISSN (International Society of Sports Nutrition).")
