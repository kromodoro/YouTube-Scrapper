from youtube import scrap_youtube_data
from sheets import save_to_sheets
import constants as const

# Lista de Canais

# Codigo fonte TV https://www.youtube.com/c/codigofontetv
# Luan Moreno https://www.youtube.com/c/LuanMorenoMMaciel
# Mais Aprendizagem https://www.youtube.com/c/MaisAprendizagemAnaLopes


if __name__ == "__main__":
    # Array de canais
    channel_ids = [
        #"UCnJNY2XuPDUvequZ0wULQdA",
        "UCxSRp7qtfPqyPToM_176ZhQ", # Taryana
        "UCnErAicaumKqIo4sanLo7vQ",
        "UCnXuqGASORXcU4gDnr_9I_w", #aprenda qualquer coisa
    ]

    data = scrap_youtube_data(channel_ids)

    save_to_sheets(data, const.SPREADSHEET_ID)
