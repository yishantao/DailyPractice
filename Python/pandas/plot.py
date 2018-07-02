# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.DataFrame({'open': [1, 2, 3, 4, 5, 6], 'close': [2, 5, 8, 6, 7, 9]})
# data.plot()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(2, 1)
# data = pd.DataFrame({'open': [1, 2, 3, 4, 5, 6], 'close': [2, 5, 8, 6, 7, 9]})
# data.plot(kind='bar', ax=axes[0], color='k')
# data.plot(kind='barh', ax=axes[1], color='g')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1)
data = pd.Series([1, 2, 2, 4, 4, 4])
data.value_counts().plot(kind='bar', ax=axes[0], color='k')
plt.show()
