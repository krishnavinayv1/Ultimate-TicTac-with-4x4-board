	def __init__(self):
                global moves
                moves=0
                global heuristic_arr1
                global block_list
                heuristic_arr1=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
                for i in range(16):
                    block_list.append([])
                block_list[0].append([0,1,2,3])
                block_list[0].append([0,5,10,15])
                block_list[0].append([0,4,8,12])
                block_list[1].append([0,1,2,3])
                block_list[1].append([1,5,9,13])
                block_list[2].append([0,1,2,3])
                block_list[2].append([2,6,10,14])
                block_list[3].append([0,1,2,3])
                block_list[3].append([3,7,11,15])
                block_list[3].append([3,6,9,12])
                block_list[4].append([4,5,6,7])
                block_list[4].append([0,4,8,12])
                block_list[5].append([1,5,9,13])
                block_list[5].append([4,5,6,7])
                block_list[5].append([0,5,10,15])
                block_list[6].append([4,5,6,7])
                block_list[6].append([2,6,10,14])
                block_list[6].append([3,6,9,12])
                block_list[7].append([3,7,11,15])
                block_list[7].append([4,5,6,7])
                block_list[8].append([0,4,8,12])
                block_list[8].append([8,9,10,11])
                block_list[9].append([8,9,10,11])
                block_list[9].append([3,6,9,12])
                block_list[9].append([2,5,9,13])
                block_list[10].append([2,6,10,14])
                block_list[10].append([8,9,10,11])
                block_list[10].append([0,5,10,15])
                block_list[11].append([3,7,11,15])
                block_list[11].append([8,9,10,11])
                block_list[12].append([12,13,14,15])
                block_list[12].append([0,4,8,12])
                block_list[12].append([3,6,9,12])
                block_list[13].append([1,5,9,13])
                block_list[13].append([12,13,14,15])
                block_list[14].append([12,13,14,15])
                block_list[14].append([2,6,10,14])
                block_list[15].append([12,13,14,15])
                block_list[15].append([3,7,11,15])
                block_list[15].append([0,5,10,15])

		pass