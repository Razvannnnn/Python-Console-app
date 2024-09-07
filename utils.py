class Utils:
    @staticmethod
    def insertion_sort(list, reverse=False, key=None, cmp=lambda x,y: x<y):
        """
        Caz favorabil O(n)
        Caz nefavorabil O(n^2)
        Caz mediu O(n^2)

        Sorteaza elementele din lista print insertie
        :param list: lista de elemente
        :return: lista ordonata
        """
        if key != None:
            for i in range(1, len(list)):
                j = i - 1
                current_element = list[i]
                while j >= 0 and cmp(key(current_element), key(list[j])):
                    list[j + 1] = list[j]
                    j = j - 1
                list[j + 1] = current_element
        else:
            for i in range(1, len(list)):
                j = i - 1
                current_element = list[i]
                while j >= 0 and cmp(current_element, list[j]):
                    list[j + 1] = list[j]
                    j = j - 1
                list[j + 1] = current_element
        if reverse == True:
            return list[::-1]
        return list

    @staticmethod
    def comb_sort(list, reverse=False, key=None, cmp=lambda x,y: x<y):
        """
        Caz favorabil O(n log n)
        Caz nefavorabil O(n^2)
        Caz mediu O(n^2/2^p) p=nr de incrementari

        Sorteaza elementele din lista prin combinari
        :param list: lista de elemnte
        :return: lista ordonata
        """
        def get_next_gap(gap):
            gap = (gap * 10) / 13
            return max(1, int(gap))

        n = len(list)
        gap = n
        swapped = True
        if key != None:
            while gap != 1 or swapped:
                gap = get_next_gap(gap)
                swapped = False

                for i in range(0, n - gap):
                    if cmp(key(list[i+gap]), key(list[i])):
                        list[i], list[i+gap] = list[i+gap], list[i]
                        swapped = True
        else:
            while gap != 1 or swapped:
                gap = get_next_gap(gap)
                swapped = False

                for i in range(0, n - gap):
                    if cmp(list[i+gap], list[i]):
                        list[i], list[i+gap] = list[i+gap], list[i]
                        swapped = True

        if reverse == True:
            return list[::-1]
        return list