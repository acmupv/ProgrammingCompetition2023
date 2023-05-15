def main():
    N, D = map(int, input().split(' '))
    case = 1
    while N != 0 or D != 0:

        if case != 1:
            print()
        print(f'Caso {case}:')
        #dictionary where we will store a list of the money for each danger level 
        # key : value -> P : []
        banks = {} 
        #Read the input and add it to the dict.
        for i in range(N):
            money, P = map(int, input().split(' '))
            #Create the key if it does not exists
            if banks.get(P) is None:
                banks[P] = []
            banks[P].append(money)
            
        alg(N, D, banks)

        N, D = map(int, input().split(' '))
        case += 1



def alg(N, D, banks):
        
        sort_dangers = sorted(list(banks.keys())) #So we can start searching from the lowest danger level

        max_money = [] #we will store here the sum of money we can get from all the banks at each danger level
        for i in sort_dangers:
            max_money.append(sum(banks.get(i)))
        
        #finding how much levels of dangers are and if is it posible to get the money
        suma = 0
        danger = 0
        while suma < D and danger < len(sort_dangers):
            suma += max_money[danger]
            danger += 1

        if suma < D:
            print('impossible')
        
        else:
            num_banks = [0] * danger
            suma = 0

            while suma < D:
                maxim = 0
                level = 0 # level doesn't representate the real danger level but its position in the array

                for i in range(danger): #we take the maximum amount of money posible within the banks availables and remove it from the array
                    try: #if the list is empty it throws an exception
                        aux = max(banks.get(sort_dangers[i]))
                        if aux > maxim:
                            maxim = aux
                            level = i
                    except:
                        pass

                banks.get(sort_dangers[level]).remove(maxim)
                suma += maxim
                num_banks[level] += 1

            for i, j in enumerate(num_banks):
                if j != 0:
                    print(f'{sort_dangers[i]} -> {j}')
        
if __name__ == '__main__':
    main()