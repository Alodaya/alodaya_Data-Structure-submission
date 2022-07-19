#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:20:29 2022

@author: ainish
"""


import IOFunctions as io

class SwimmingClub:
    def __init__(self, Data = None):
        self.Data       = Data
        self.AllSlots   = []
        self.Overlap    = []
        self.TotalSlots = 0
        self.MaxCoverage = 0
        return
    
    def GetRawData(self,Data):
        self.Data = Data
        return
    
    def TotalSlotsCovered(self):
        '''
        Member function in SwimmingClub to calculate the total number of slots 
        that are covered by all available guards.
        Returns
        -------
        None.
        '''

        for slot in self.AllSlots:
            START = 0
            STOP  = 1
            self.TotalSlots = self.TotalSlots + slot[STOP]-slot[START]+1

        return 
     
    def CheckCoverage(self):
        '''
        Member function that generates a list of all slots covered when all guards are available
        The function creates a list of time slots, where each slot consists of contiguous intervals covered
        Disparate slots lead to generation of a new interval
        
        In addition, the function also creates a list of slots that have more than over guard covering the slot

        Returns
        -------
        None.

        '''
        for slot in self.Data:
            overlap = []
            START   = 0
            STOP    = 1
            LAST    = -1
            ''' Add Slots to all coverage '''
            try:
                
                if slot[START] > self.AllSlots[LAST][STOP]+1:
                    ''' If New Slot begins after current ends, there is no overlap add to All coverage '''
                    self.AllSlots.append(slot.copy())
                    
                else:
                    ''' In case there is coverage, first check if there is any overlap '''
                    overlap = [slot[START], min(self.AllSlots[LAST][STOP], slot[STOP])] 
                    if overlap[START]<=overlap[STOP]:
                        try:
                            if overlap[START] > self.Overlap[LAST][STOP]+1:
                                self.Overlap.append(overlap)
                            else:
                                self.Overlap[LAST][STOP] = max(self.Overlap[LAST][STOP], overlap[STOP])
                        except:
                            self.Overlap.append(overlap)
                            
                    self.AllSlots[LAST][STOP] = max(self.AllSlots[LAST][STOP], slot[STOP])
            except:
                self.AllSlots.append(slot.copy())
                continue
        return
    

    
    def FindMinUniqueSlots(self):
        '''
        Member function to find the guard with the fewest number of unique slots.
        Subtracting this from Total coverage gives us the maximum coverage if one guard was to be fired.
        Returns
        -------
        None.

        '''
        START, STOP = 0,1
        UniqueSlots = self.TotalSlots
        newstart = 0

        for guard in self.Data:
            num_overlaps = 0
            for i in range(newstart, len(self.Overlap)):
                slot = self.Overlap[i]
                if guard[START] > slot[STOP]:
                    '''placeholder to find optimised starting point to run intersection search'''
                    newstart +=1
                    continue
                elif guard[STOP] < slot[START]:
                    ''' Given sorted data, once end of slot is found, break out of the loop '''
                    break
                else:
                    num_overlaps = num_overlaps + min(guard[STOP], slot[STOP]) - max (guard[START], slot[START]) + 1
            
            UniqueSlots = min(guard[STOP] - guard[START] + 1 - num_overlaps, UniqueSlots)
            if UniqueSlots == 0:
                break
        
        self.MaxCoverage = self.TotalSlots-UniqueSlots      
        return
    
    def RunSimulation(self):
        self.CheckCoverage()
        self.TotalSlotsCovered()
        self.FindMinUniqueSlots()
        return
    
                

                
if __name__ == '__main__':
    
    for i in range(1,11):
        data = io.ProcessInput(i)
        S = SwimmingClub(data)
        S.RunSimulation()
        io.WriteOutput(i, content = S.MaxCoverage)

    