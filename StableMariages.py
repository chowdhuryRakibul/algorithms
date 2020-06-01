'''
Write a Python function stableMatching(n, menPreferences, womenPreferences) that gets the number n of women and men, preferences of all women and men, and outputs a stable matching.
The function should return a list of length n, where ith element is the number of woman chosen for the man number i.
'''

def stableMatching(n, menPreferences, womenPreferences):
    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                      
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]
       
        
        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
        if currentHusband == None:
          #No Husband case
          #"She" accepts any proposal
          womanSpouse[she] = he
          manSpouse[he] = she
          #"His" nextchoice is the next woman
          #in the hisPreferences list
          nextManChoice[he] = nextManChoice[he] + 1
          #Delete "him" from the 
          #Unmarried list
          unmarriedMen.pop(0)
          #in case you are not familiar with pop just use
          #del unmarriedMen[0]
          #this will delete the first item and 
        else:
          #Husband exists
          #Check the preferences of the 
          #current husband and that of the proposed man's
          currentIndex = herPreferences.index(currentHusband)
          hisIndex = herPreferences.index(he)
          #Accept the proposal if 
          #"he" has higher preference in the herPreference list
          if currentIndex > hisIndex:
             #New stable match is found for "her"
             womanSpouse[she] = he
             manSpouse[he] = she
             nextManChoice[he] = nextManChoice[he] + 1
             #Pop the newly wed husband
             unmarriedMen.pop(0)
             #Now the previous husband is unmarried add
             #him to the unmarried list
             unmarriedMen.insert(0,currentHusband)
          else:
             nextManChoice[he] = nextManChoice[he] + 1
             
    return manSpouse
    
# Complexity Upper Bound : O(n^2)



#main function
    
n = 4

'''
let according to the video https://www.youtube.com/watch?v=Qcv1IqHWAzg
menList --> Bingley -> 0, Darcy -> 1, Collins -> 2, Wickham -> 3
womenList --> Jane -> 0, Elizabeth -> 1, Lydia -> 2, Charlotte -> 3
'''
womenPreferences = [[0,1,2,3],
                    [3,1,0,2],
                    [0,3,1,2],
                    [0,3,1,2]
                    ]
menPreferences = [[0,1,2,3],
                  [0,1,2,3],
                  [1,0,3,2],
                  [2,0,1,3]
                  ]

stableMatching(n,menPreferences,womenPreferences)
'''
This function returns the following mapping

ith element   --   Number of woman chosen
-------------------------------------
Bingley (0)   --   Jane (0)
Darcy (1)     --   Elizabeth (1)
Collins (2)   --   Charlotte (3)
Wickham (3)   --   Lydia (2)

'''