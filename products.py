"""
Author: <Suyue Wang> (<29672031>)

In this assignment we implement the backend of an intelligent product
search engine where potential customers can search a database of products
characterised by different features taking into account the customer's
preferences.

Functions for 1 and 2 are due in Part 1 of the assignment. Functions
for 3 and 4 are due in Part 2.

As a global conventions, to select products based on hard criteria,
we will use Python objects representing conditions. These are represented
as triples (i, c, v) where i is an integer feature index, c is a relation
symbol in ['<', '<=' '==', '>=', '>', '!='], and v is some feature value.
A product (represented by a feature vector) _satisfies_ condition (i, c, v)
if its i-th feature value is in relation c with the value v. This will be
implemented in a function 'satisfies'. For example:
>>> inexpensive = (4, '<=', 1000)
>>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
True
>>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
False

For more information see the function documentations below and the
assignment sheet.
"""


# Part 1 (due Week 6) #


def satisfies(product, cond):
    """
    Determines whether a product satisfies a given condition.

    Input : A product feature list (product() and a condition
            (cond) as specified above.
    Output: True if cond holds for the product otherwise False.

    For example, consider the following conditions:
    >>> inexpensive = (4, '<=', 1000)
    >>> large_screen = (2, '>=', 6.3)
    >>> apple_product = (1, '==', 'Apple')

    With this the function behaves as follows:
    >>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
    True
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], large_screen)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], apple_product)
    True

    <Since the output of this function returns a boolean statement (True or False).
    I will needed to assign a condition for each relation symbols (eg. ==, <=, !=). 
    Given the first element (element[x]) in the condition relates to the xth element 
    in the list for each product (product[x]) I could compare them using the boolean to obtain my output.

    It seems that the for loop in my satisfied function is unnecessary when I only need to run this function. 
    But when I want to use this function as a sub function for def selection. 
    If my code starts with x=cond[0], there will shows up a Type error. 
    So I have added the for loop in this function to overcome this issue. >

    <In is function my idea to solve the problem was really straight forward. 
    If the 2nd element in condition (cond[2]) is the same as the symbols in each condition statement. 
    Then I will use another boolean to test whether the 3rd cond element (cond[2]) 
    and the xth in list product (product[x]) follows the relation symbols. And will print the result in 'Ture' or 'False'.
    
    I have used a for loop for variable i in the range from 0 to the lenght of 'cond' (li=len(cond)).
    As I have mentioned above, this for loop is used for the implementation of def satisfied(p,c) 
    to be use in the seletion function. By doing so, in the selection function, 
    I will be able to loop through each product (product[i]) in the lists of products 
    to see if they have matched their conditions and return as Ture or False.>

    """

    li=len(cond)
    for i in range(0,li):
        x=cond[0]
        if cond[1] == '==':
            return product[x] == cond[2]
        elif cond[1] == '<':
            return product[x] < cond[2]
        elif cond[1] == '>':
            return product[x] > cond[2]
        elif cond[1] == '<=':
            return product[x] <= cond[2]
        elif cond[1] == '>=':
            return product[x] >= cond[2]
        else:
            return product[x] != cond[2]



def selection(products, conditions):
    """
    Filters a given product table by a list of conditions.

    Input : A product table (products) and a list of conditions
            (conditions) consisting of triples (i, c, v) as specified
            in the module documentation.
    Output: The list of products satisfying all conditions.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price.
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    Then the function behaves as follows:
    >>> large_screen = (2, '>=', 6.3)
    >>> cheap = (4, '<=', 400)
    >>> selection(phones, [cheap, large_screen])
    [['Reno Z', 'Oppo', 6.4, 4035, 397]]
    >>> not_apple = (1, '!=', 'Apple')
    >>> selection(phones, [not_apple])
    [['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <With this function I want it to return the list of products which satisfied the condition. 
    So I have connected the selection function with the satisfied function, so whenever the product[i] has 
    return Ture under the condition given in selection(p,c). I will add them to a empty list variable 'res=[]'. 
    But I find it challenging for the positioning of the conditioning statement (if re:) .
    Beacuse different positions results differently, 
    so I have to make sure the first if statement if after 'for j in range(0,l)' and my 
    second if statement is aline with the 'for j' loop' so that if (boolean) re is Ture after running satisfied function.
    Then add the related product[i] in to the 'res' list.  

    I also find a problem with my code before assigning the variable re to be Ture 're=Ture'. 
    The output of selection function when there are more then one conditions, and the product satisfied only one of the conditions.
    They could still shown in my output. To solve this problem, 
    I have added 2 line in my code,'re=Ture' and a another boolean expression 'if re: re=statisfied(p[i],c[j])'. This if statement
    helps with my problem, beacuse it test for every product[i] and condition[i][j] to be Ture before proceeding to the next step.>

    <I have use 2 ‘for loops’ in the selection function. The first one goes for variable i in range of product length.
    The second 'for loop' is for j in range of condition length. This is because the input variable condition and product have different length.
    And for each product[i] I want it to be tested by condition[j].
    The 're = Ture' has been explained as the paragrapgh above, it helps my code to identidy whether the satisfies function returns a Ture or False.
    If the satisfies return False, and given re is Ture. This will lead to a False. Which the relevent product[i] will not being added into the list res.
    The last part of my code to get the result is using the res.append() function to add the product[i] into list 'res' when it passes the if statement.>

    """

    res=[]
    pro=len(products)
    l=len(conditions)
    for i in range(0,pro):
        re = True
        for j in range(0,l):
            if re:
                re=satisfies(products[i],conditions[j])
        if re:
            res.append(products[i])
    return res
    



def linearly_ranked(products, weights):
    """
    Ranks products in order of preference as specified by a linear
    weight vector.

    Input : Product table (products) with n columns, list of
            weights of length n containing at position i the
            linear weight for product feature column i or None if
            no weight is specified for column i
            (must be None for non-numeric column).
            At least one weight must be different from None.
    Output: A new table containing all products from the input table
            in decreasing order of the linear score given, for a product
            prod in products, by the sum of prod[i]*weights[i] over
            all column indices i with weights[i]!=None.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This leads to the following behavior
    >>> battery = [None, None, None, 1, None]
    >>> linearly_ranked(phones, battery)
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['iPhone11', 'Apple', 6.1, 3110, 1280]]
    >>> screen_battery_price = [None, None, 10, 1/1000, -1/100]
    >>> linearly_ranked(phones, screen_battery_price)
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['iPhone11', 'Apple', 6.1, 3110, 1280]]

    The input table is not changed by the function. That is
    after calling it, we still have:
    >>> phones
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <To find the decreasing order of products under the given condition of the weights. 
    Firstly I need to calculate the weight (the once that are not 'None') for each product[i]. 
    By using the wieghts I will be able to sort the order for the list of products.
    But the problem is that I have to locate this weights in the variable that I use to sort. Otherwise, it won't change anything.
    So I have add an extra element (count) in every product's list to be the calculated weight for that particular product[i].
    Then I use the adjusted product list into the sorting part. But when I was running my code for testing. Another problem occured.
    If the input variable is only phones. And it is expecting to return the original list of phones/products. 
    But my code will change the order of them becasue it still sorts the list. So I have added a new empty list called pro (pro=[])
    to save the adjusted product list including the added weights. And I keep using this 'pro' list to sort.
    This can avoid changing the input order but return the output based on given conditions for weights.>

    <In this function I have used 3 for loops. 
    This first for loop is for the i variables in range of the lenght of product. And will add each product[i] into the empty list 'pro'.
    Assigning 0 to a new variable count is used to record the calculated weight for each product[i] in the second for loop.
    The loop for j in range(0,w) is a for loop of variable j in the range of length of weights. 
    While I only need the element in weights that is not 'None'. So I used an if statement to filter out the usable element[j]
    in weight which is the once that are not repersenting 'None'. The count variable recorded the calculated weights by 
    multiplying the sum of each weights[j] to the relatied product[i] in the jth position. And then I add 'count' to the end of every product (pro[i]).
    
    The sorting part is in a similar way to the insort function. But given we want an output that is in a decreasing order.
    In the while loop, the conditions are the pro[i] is greater than 0, and for the last element in pro[i] 
    is greater than the last element in pro[i-1]. Then swap the order of this two list. 
    And keep looping in the while loop until i is less or equal to 0 so that all inner list in pro(product) has been sorted.

    Lastly, for i variables in range of the length of products.
    I used the pro[i].pop() to remove the last element in the inner list in pro. So the output will be the sorted list of product by weights>

    """
    n=len(products)
    w=len(weights)
    pro=[]
    for i in range(0,n):
        pro.append(products[i])
        count=0
        for j in range(0,w):
            if weights[j] is not None:
                count= count + pro[i][j]*weights[j]
        pro[i].append(count)
        while i>0 and pro[i][-1]>pro[i-1][-1]:
            pro[i-1],pro[i]=pro[i],pro[i-1]
            i=i-1
    for i in range(0,n):
        pro[i].pop()
    return pro



# Part 2 (due Week 11) #


def relevant(products, preferences):
    """
    Filters a product table for relevant products given user preferences.

    Input : A product table (products) and a list of preferences, where
            each preference is a pair (i, p) with i being the index of to a
            numeric column in products and p is either +1 or -1 depending
            on whether the user considers feature i to be positive or negative.
    Output: A new list of products that are relevant with respect to the
            preferences. A product is relevant if it is not dominated by another
            product, which is defined as follows:
            - prod1 dominates prod2 with respect to preference (i,p) if
              prod1[i] > prod2[i] in case p=1 (or prod1[i] < prod2[i] in case p=-1)
            - prod1 dominates prod2 if prod1 dominates prod2 with respect to at
              least one specified preference and not prod2 does not dominate prod2
              with respect to any specified preference

    For example:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S21', 'Samsung', 6.2, 3300, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3700, 497],
    ...           ['P30 Pro', 'Huawei', 6.4, 3500, 398],
    ...           ['R17 Pro', 'Oppo', 6.6, 3200, 457],
    ...           ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> large_battery_but_cheap = [(3,1), (4,-1)]
    >>> relevant(phones, large_battery_but_cheap)
    [['Nova 5T', 'Huawei', 6.26, 3700, 497], ['P30 Pro', 'Huawei', 6.4, 3500, 398], ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> big_screen = [(2,1)]
    >>> relevant(phones, big_screen)
    [['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> relevant(phones, big_screen_but_cheap)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_large_battery = [(2,1),(3,1)]
    >>> relevant(phones, big_screen_large_battery)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457], ['Pixel 3', 'Google', 6.3, 3800, 688]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    <Paragraph on computational complexity.>

    """
    n=len(products)
    while 





    res=[]
    re=[]
    for i in range(0,len(products)):
        for ii in range(0,len(products)):
            for j in range(0,len(preferences)):
                k=preferences[j][0]
                if preferences[j][1]==1 and products[i][k]>products[ii][k]:
                    re=products[i]
                elif preferences[j][1]==1 and products[i][k]<products[ii][k]:
                    re=products[ii]
                elif preferences[j][1]!=1 and products[i][k] < products[ii][k]:
                    re= products[i]
                else:
                    return re=products[ii]
                res.append(re)
            return res
            
                


if preference[j][1]==1:
    
        
    pass
pre=[(2,1)]
p=[6.26,6.6,6.4]

def pro(p,pre):
    n=len(p)
    po=len(pre)
    for i in range(n-1):
        for j in range(po):
            if p[i]>p[i+1] and pre[j][1]==1:
                return True
            elif p[i]<p[i+1]and pre[j][1]!=1:
                return True
            else: 
                return False
        return False
print(pro(p,pre))
    

def inferred_conditions(pos_examples, neg_examples):
    """
    Infers selection conditions from positive and negative product examples.

    Input:  two non-empty lists of products, pos_examples and neg_examples,
            based on the same list of _numeric_ features
    Output: Set of conditions conds such that
            len(selection(neg_examples, conds)) is minimal
            under the constraint that
            selection(pos_examples, conds)==pos_examples

    Let's first consider a simple example with one column:
    >>> pos_ex = [[10], [14]]
    >>> neg_ex = [[4], [11], [20]]
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [[10], [14]]
    >>> selection(neg_ex, conds)
    [[11]]

    For a more complex example, let's go back to our
    phone application. Assume the user has specified
    the following positive and negative examples.
    >>> pos_ex = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> neg_ex = [['Galaxy S20', 'Samsung', 6.46, 3000, 1348],
    ...           ['V40 ThinQ', 'LG', 5.8, 3100, 598],
    ...           ['7T', 'OnePlus', 6.3, 3300, 1200]]

    Another table of new phones could be as follows.
    >>> new_phones = [['Galaxy S9', 'Samsung', 5.8, 3000, 728],
    ...               ['Galaxy Note 9', 'Samsung', 6.3, 3600, 700],
    ...               ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    Then the conditions found by the function should behave
    as follows:
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> selection(neg_ex, conds)
    [['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> selection(new_phones, conds)
    [['Galaxy Note 9', 'Samsung', 6.3, 3600, 700], ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    <Paragraph on computational complexity.>

    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

