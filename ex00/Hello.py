ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = ft_list[1].replace("tata!", "World")
ft_tuple = (ft_tuple[0],ft_tuple[1].replace("toto!","France"))
ft_set.remove("tutu!")
ft_set.add("Paris")

ft_dict["Hello"] = ft_dict["Hello"].replace("titi!","42Paris")


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)