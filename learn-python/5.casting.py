#%% Casting -cambio entre tipos
# int() convierte desde str y float -> int
# float() convierte desde str, float o int -> fload
# str() muchos datos se pueden castear a str

my_int = 123
my_float = 3.1415
my_str = " Soy un string:"
new_int = int(my_float)
new_float = float(my_int)

new_str1 = str(my_int)
new_str2 = str(my_float)
print("new_int is", type(new_int).__name__)
print("new_float is", type(new_float).__name__)


print("new_str1 is", type(new_str1).__name__)
print("new_str2 is", type(new_str2).__name__)
# %%
