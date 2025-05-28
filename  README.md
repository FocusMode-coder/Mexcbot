


# LucianoPro_Robinhood_Signals_AI

🚀 Bot de señales profesionales para trading en Robinhood, basado en análisis real de mercado desde MEXC.

## 🔧 ¿Qué hace este bot?
Este bot analiza el mercado de ETH y otras oportunidades usando señales tipo Sniper + Guardian + Whale. Te envía recomendaciones reales a tu Telegram como:
- "Comprá ahora un CALL a $65 exp. 6/7"
- "Salí en 5 minutos, señal bajista detectada"

## ✅ Requisitos
- Cuenta en MEXC con claves API (ya configurado en el sistema)
- Cuenta de Telegram con bot creado (ya configurado)
- Conexión a Render para ejecución 24/7

## 🛠️ Instalación y deploy (modo fácil)

1. **Cloná este repositorio o subilo a tu GitHub**
2. **Conectá tu GitHub a [Render.com](https://render.com)**
3. **Seleccioná este repositorio y Render usará automáticamente `render.yaml`**
4. **El bot se desplegará y empezará a funcionar solo**
5. **Recibirás señales automáticas en tu Telegram**

## 📦 Estructura principal

```
LucianoPro_Robinhood_Signals_AI/
├── core/
│   └── main.py
├── strategy/
│   └── analyzer.py
├── telegram/
│   └── send.py
├── market/
│   └── market.py
├── utils/
│   ├── helpers.py
│   ├── math_tools.py
│   ├── text_cleaner.py
│   └── time_utils.py
├── logs/
│   └── signals.log
├── test/
│   └── test_market.py
├── render.yaml
├── requirements.txt
└── README.md
```

## 📬 Contacto
Creado por Luciano y LucianoAI (modo Dios). Consultas: vía Telegram privado.
