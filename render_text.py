"""
Render Latex
"""
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt

font_path = r'C:\Users\Brent\Fonts\Roboto_Mono\static\RobotoMono-Regular.ttf'  # For Regular Text
F_PROP = fm.FontProperties(fname=font_path)


def render(text: str, save: bool = False, font_size: int = 5):
    plt.rcParams['mathtext.default'] = 'rm'
    plt.axis('off')
    if not save:
        plt.rcParams['figure.dpi'] = 150

    plt.text(
        0.5, 0.5,
        text.strip(),
        fontsize=font_size,
        ha='center', va='center',
        fontproperties=F_PROP
    )
    if save:
        # plt.savefig('C:/Users/Brent/Downloads/formula.svg', format='svg')
        plt.savefig('C:/Users/Brent/Downloads/temp.png', format='png')
    else:
        plt.show()


if __name__ == '__main__':
    #         render(r'''
    # $\sqrt{2}$
    # $A_S=1^2$
    # $A_L=(\sqrt{2})^2$
    # $ratio=1:2$
    #     ''', save=True)
    render(r'''
$\frac{1}{2}\left(\sqrt{1+(2aA+b)^2}(2aA+b)+\ln|\sqrt{1+(2aA+b)^2}+2aA+b|\right)$
'''.strip(), font_size=15, save=False)
