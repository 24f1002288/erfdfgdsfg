# def repeat_msg(message, n):
#   if n==0:
#     return None
#   print(message)
#   repeat_msg(message, n-1)

# repeat_msg("hello",5)

# def repeat_msg(m:str, n:int):
#   print(m*n,"\n")

# repeat_msg("hello",5)

def sum_n(n):
  if n==0:
      return 0
        else:
            return n+sum_n(n-1)
              
              # print(sum_n(4))

              def count_digits(n):
                if n==0:
                    return 0
                      else:
                          return 1+count_digits(n//10)
                            
                            def count_digits(n):
                              n = str(n)
                                if n == '' or n == '0':
                                    return 0
                                      else:
                                          return 1+ count_digits(n[1:])

                                          #print(count_digits(87634))

                                          def custom_len(lst):
                                            if lst==[]:
                                                return 0
                                                  else:
                                                      return 1+custom_len(lst[1:])

                                                      # print(custom_len([1,5,6]))


                                                      def fib(n):
                                                        if n == 0 :
                                                            return 0
                                                              elif n==1:
                                                                  return 1
                                                                    else:
                                                                        return fib(n-1)+fib(n-2)

                                                                        print(fib(7))

                                                                        # [1, [2, 3], [4, [5]]]
                                                                        [[]]
                                                                        def deep_sum(lst):
                                                                          if lst == []:
                                                                              return 0 
                                                                                elif lst == [[]]:
                                                                                    return 0
                                                                                      else:
                                                                                          return lst + sum(lst[lst] - 1)
                                                                                            

                                                                                            # [[2,3]]
                                                                                            def deep_sum(lst):
                                                                                              if lst==[]:
                                                                                                  return 0
                                                                                                    else:
                                                                                                        return sum(lst[1:2])+deep_sum(lst[1:])
                                                                                                          
                                                                                                          # print(deep_sum([1,[2,3],7,0]))

                                                                                                          print([1,[2,3],7,0][1:2])


                                                                                                          def deep_sum(l1):
                                                                                                            total = 0
                                                                                                              for elem in l1:
                                                                                                                  if type(elem) == int or  type(elem) == float:
                                                                                                                        total += elem
                                                                                                                            else:
                                                                                                                                  total += deep_sum(elem)
                                                                                                                                    return total

                                                                                                                                    # deep_sum([1, [2, 3], [4, [5]]])

                                                                                                                                    print(type(2) == int)

                                                                                                                                    