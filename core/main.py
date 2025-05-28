from ..strategy.analyzer import analizar_mercado
from ..telegram.messenger import enviar_mensaje_telegram
from .logger import log_signal

def main():
    try:
        señal = analizar_mercado()

        if señal:
            mensaje = (
                f"⚡️ Señal detectada:\n"
                f"🔍 Activo: {señal['activo']}\n"
                f"📈 Tipo: {señal['tipo'].upper()}\n"
                f"🎯 Strike: {señal['strike']} | Expira: {señal['exp']}\n"
                f"🧠 Recomendación: {señal['recomendacion']}\n"
                f"🔗 Ejecutá en Robinhood si te cierra."
            )
            enviar_mensaje_telegram(mensaje)
            log_signal(señal)
        else:
            info = "🕵️ No se detectaron señales válidas en este escaneo."
            enviar_mensaje_telegram(info)
            log_signal({"info": info})

    except Exception as e:
        error_msg = f"❌ Error en ejecución del bot: {str(e)}"
        enviar_mensaje_telegram(error_msg)
        log_signal({"error": error_msg})

if __name__ == "__main__":
    main()