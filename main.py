import math 

no_figures = input()

no_figures = int(no_figures.split(' ')[0])

def calculate_areas(fig_no : int):
    sum_of_areas = 0

    for i in range(fig_no):
        figure_features = input()

        figure_features = figure_features.split(' ')
        if len(figure_features)>3:
            return "Błąd: można podać maksymalnie 3 liczby"
        elif len(figure_features) == 1:
            sum_of_areas += math.pi*math.pow(float(figure_features[0]),2)
        elif len(figure_features)==2:
            sum_of_areas += float(figure_features[0]) * float(figure_features[1]) 
        elif len(figure_features)==3:
            p = (float(figure_features[0]) + float(figure_features[1]) +  float(figure_features[2]))/2
            sum_of_areas += math.sqrt(p* (p-float(figure_features[0]))* (p-float(figure_features[1]))*(p-float(figure_features[2])))

    return round(sum_of_areas,2)


print(calculate_areas(no_figures))