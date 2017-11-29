from  basic.bupt_2017_11_28.type_deco import prt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi,50)
s = pd.Series(index=x,data=np.sin(x))
s.plot(kind = "line")
plt.show()
