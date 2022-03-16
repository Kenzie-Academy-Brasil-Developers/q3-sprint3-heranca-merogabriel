from classes.copo import Copo
from classes.recipiente import Recipiente


if __name__ == "__main__":
    copo_comum = Copo(300)
    copo_comum.encher('cafe')

    print(copo_comum.__repr__())