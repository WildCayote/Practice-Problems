import copy

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        current = 1
        right = 2

        # first round filling
        count = 0
        while right < len(height):
            if (height[current] < height[left]) and (height[current] < height[right]):
                addition = min(height[left], height[right]) - height[current]
                count += addition
                height[current] += addition
            
            left += 1
            current += 1
            right += 1
        
        # fill the remaining
        left = 0
        current = 1
        right = 2
        second_count = 0
        while right < len(height):
            if (height[current] < height[left]) and (height[current] <= height[right]):
                height_copy = copy.deepcopy(height)
                new_right = right

                # look for a building that will be at least 1 block higher than the current level
                found = False 
                while new_right < len(height):
                    # check if the new right is bigger than the current, then break 
                    if height_copy[new_right] > height_copy[current]:
                        found = True
                        break
                    new_right += 1
                
                # fill in the watter to the min of the left and the new count
                if found:
                    # print(height_copy)
                    new_current = current
                    new_left = left
                    minimum_wall = min(height_copy[new_right], height_copy[new_left])
                    while new_current < new_right:
                        addition = minimum_wall - height_copy[new_current]
                        height[new_current] += addition
                        second_count += addition

                        new_current += 1
                        new_left += 1
                    # height = copy.deepcopy(height)
                    # print(f'[{left}, {current}, {right}]')
                
                else:
                    # print('here')
                    left += 1
                    current += 1
                    right += 1
            else:
                left += 1
                current += 1
                right += 1

            # print(f'{left}, {current}, {right}')

        count += second_count 
        
        return count



if __name__ == '__main__':
    answer = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    answer_1 = answer.trap(height)
    print(f"Result for test case 1: {answer_1}")

    height = [4,2,0,3,2,5]
    answer_2 = answer.trap(height)
    print(f"Result for test case 1: {answer_2}")

    height =[6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]  # expected answer 83
    answer_2 = answer.trap(height)
    print(f"Result for test case 1: {answer_2}")