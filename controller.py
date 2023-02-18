import view
import model


num_classes = view.start()
num_lesson = view.choose_lesson()
dict_classes = model.classes_choose(num_classes)

view.print_classes(num_lesson, dict_classes)

num_who = view.who_go(dict_classes)

print(num_who)