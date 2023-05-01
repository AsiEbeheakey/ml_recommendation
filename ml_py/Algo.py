'''
import pandas as pd
# 
pref_cols = ['staff_id', 'menu_id', 'pref_scale']
preferences = pd.read_csv('preferences.csv', sep=',',names=pref_cols)
# 
menu_cols = ['menu', 'menu_id']
menu = pd.read_csv('menu.csv',sep=',', names=menu_cols)
# 
preferences_output = pd.merge(menu, preferences)
# 
preferences_output.head()
# 
preferences_output.head(10)

# 
menu_preferences = preferences_output.pivot_table (index=['staff_id'],columns=['menu'], values='pref_scale')
menu_preferences.head()

# 
fufu_goatsoup = menu_preferences['Fufu with goat light soup']
fufu_goatsoup.head()

# 
similarMenus = menu_preferences.corrwith(fufu_goatsoup)
similarMenus = similarMenus.dropna()
df = pd.DataFrame(similarMenus)
df.head(10)
'''