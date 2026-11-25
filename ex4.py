import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# 1) Variáveis linguísticas e seus universos
horas = ctrl.Antecedent(np.arange(0, 12.1, 0.1), 'horas')
desp  = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'despertares')
qual  = ctrl.Consequent(np.arange(0, 101, 1), 'qualidade')

# 2) Fuzzificação: funções de pertinência
horas['poucas']    = fuzz.trapmf(horas.universe, [0, 0, 5, 7])
horas['adequadas'] = fuzz.trapmf(horas.universe, [6, 7.5, 8.5, 9.5])
horas['muitas']    = fuzz.trapmf(horas.universe, [9, 10, 12, 12])

desp['poucos'] = fuzz.trapmf(desp.universe, [0, 0, 1, 3])
desp['alguns'] = fuzz.trimf(desp.universe, [2, 4, 6])
desp['muitos'] = fuzz.trapmf(desp.universe, [4, 6, 10, 10])

qual['ruim']    = fuzz.trapmf(qual.universe, [0, 0, 25, 45])
qual['regular'] = fuzz.trimf(qual.universe, [30, 50, 70])
qual['boa']     = fuzz.trapmf(qual.universe, [55, 75, 100, 100])

# 3) Base de regras (E = mínimo, OU = máximo)
regras = [
    ctrl.Rule(horas['poucas'], qual['ruim']),
    ctrl.Rule(horas['adequadas'] & desp['poucos'], qual['boa']),
    ctrl.Rule(horas['adequadas'] & desp['alguns'], qual['regular']),
    ctrl.Rule(horas['adequadas'] & desp['muitos'], qual['ruim']),
    ctrl.Rule(horas['muitas'] & desp['poucos'], qual['regular']),
    ctrl.Rule(horas['muitas'] & (desp['alguns'] | desp['muitos']), qual['ruim']),
]

# 4) Inferência + defuzzificação (centroide)
sistema = ctrl.ControlSystemSimulation(ctrl.ControlSystem(regras))
sistema.input['horas'] = 6.5
sistema.input['despertares'] = 2
sistema.compute()
print(f"Qualidade do sono: {sistema.output['qualidade']:.1f}/100")

# Gráficos das funções de pertinência e do resultado
horas.view()
plt.savefig("pertinencia_horas.png", dpi=150)
plt.close()

desp.view()
plt.savefig("pertinencia_despertares.png", dpi=150)
plt.close()

qual.view(sistema)
plt.savefig("resultado_qualidade.png", dpi=150)
plt.close()