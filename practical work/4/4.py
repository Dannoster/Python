import pandas as pd
from matplotlib import pyplot as plt
# from matplotlib import ticker
import os

def scale_axis_like_Artem():
    xmin, xmax, ymin, ymax = plt.axis()
    ax = plt.gca()
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    # ax.grid(which='major',
    #     color = 'k')

    # #  Включаем видимость вспомогательных делений:
    # ax.minorticks_on()
    # #  Теперь можем отдельно задавать внешний вид
    # #  вспомогательной сетки:
    # ax.grid(which='minor',
    #         color = 'gray',
    #         linestyle = ':')
    new_ymin = ymin - (ymax - ymin)
    nex_ymax = ymax + (ymax - ymin)
    ax.set_ylim([new_ymin, nex_ymax])

def make_graphs(is_Artem: bool = False, teor_color="b", exp_color="r"):
    df = pd.read_csv("res.csv", sep=";")
    for i in range(18):
        current_df = df[df["Номер графика"] == i+1]

        title_1: str = current_df.iloc[0]['Подпись']
        title_2: str = current_df.iloc[0]['Параметры']

        left_bracket = title_1.find("(");   right_bracket = title_1.find(")")
        x_label = title_1[left_bracket+1 : right_bracket]
        if x_label == "E":
            x_label += ", МэВ"
        y_label = title_1[left_bracket-2 : left_bracket]

        x = current_df["E"]
        y_teor = current_df["Эксперимент(t3)Теория(t2)"]
        y_exp = current_df["Эксперимент(t2)Теория(t3)"]
        time_scale = "с"
        if y_label == "t3":
            y_teor, y_exp = y_exp, y_teor
            time_scale = "мин"

        plt.title(title_1 + "\n" + title_2)
        plt.xlabel(x_label);    plt.ylabel(f"{y_label}, {time_scale}")
        plt.grid(which="both", linestyle=":")
        plt.plot(x, y_teor, label="Теория", color=teor_color)
        plt.plot(x, y_exp, label="Эксперимент", color=exp_color)
        plt.legend()
        save_dir = f"{title_1}.png"
        if is_Artem:
            scale_axis_like_Artem()
            try:
                os.mkdir("Artem")
            except FileExistsError:
                pass
            save_dir = f"Artem/{title_1}.png"
        plt.savefig(save_dir)

        plt.clf()
        plt.cla() 
        plt.close()

        print(f"Ended {i+1} graph")

# make_graphs()
make_graphs(is_Artem=True, exp_color="magenta", teor_color="lime")