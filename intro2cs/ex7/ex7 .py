from SolveLinear3 import solve_linear_3


def is_point_inside_triangle(point, v1, v2, v3):
	first_equation=[v1[0],v2[0],v3[0]]
	second_equation=[v1[1],v2[1],v3[1]]
	third_equation=[1,1,1]
	coefficeients_list=[first_equation,second_equation,third_equation]
	right_hand_list=[point[0],point[1],1]
	abc=solve_linear_3(coefficeients_list,right_hand_list)
	a=abc[0]
	b=abc[1]
	c=abc[2]
	is_inside=(1>a>0 and 1>b>0 and 1>c>0)
	return (is_inside,abc)



def create_triangles(list_of_points):
	num_of_points=len(list_of_points)
	triangle1=(list_of_points[0],list_of_points[1],list_of_points[2])
	triangle2=(list_of_points[2],list_of_points[3],list_of_points[0])
	all_triangles=[triangle1,triangle2]	
	num_of_triangles=2
	j=0
	for i in range(4,num_of_points):
		for j in range(0,num_of_triangles):
			triangle=is_point_inside_triangle(list_of_points[i],
				all_triangles[j][0],all_triangles[j][1],all_triangles[j][2])
			if triangle[0]==True:
				new_tri1=(list_of_points[i],all_triangles[j][0],
														all_triangles[j][1])
				new_tri2=(list_of_points[i],all_triangles[j][0],
														all_triangles[j][2])
				new_tri3=(list_of_points[i],all_triangles[j][1],
														all_triangles[j][2])
				all_triangles.remove(all_triangles[j])
				all_triangles.append(new_tri1)
				all_triangles.append(new_tri2)
				all_triangles.append(new_tri3)
		num_of_triangles+=2
	return (all_triangles)

	

def do_triangle_lists_match(list_of_points1, list_of_points2):
	triangles_list1=create_triangles(list_of_points1)
	triangles_list2=create_triangles(list_of_points2)
	for i in range(0,len(list_of_points1)):
		for j in range(0,len(triangles_list1)):
			a1=triangles_list1[j][0]
			b1=triangles_list1[j][1]
			c1=triangles_list1[j][2]
			a2=triangles_list2[j][0]
			b2=triangles_list2[j][1]
			c2=triangles_list2[j][2]
			if list_of_points1[i]==a1 or list_of_points1[i]==b1 or list_of_points1[i]==c1:
				if list_of_points2[i]!=a2 and list_of_points2[i]!=b2 and list_of_points2[i]!=c2:
					return False
	return True

def get_point_in_segment(p1,p2,alpha):
	x=p1[0]*(1-alpha)+p2[0]*alpha
	y=p1[1]*(1-alpha)+p2[1]*alpha
	v=(x,y)
	return (v)


def get_intermediate_triangles(source_triangles_list, target_triangles_list,
                                                                 alpha):
	new_triangles=[]
	for i in range(0,len(source_triangles_list)):
		first_point=get_point_in_segment(source_triangles_list[i][0],target_triangles_list[i][0],alpha)
		second_point=get_point_in_segment(source_triangles_list[i][1],target_triangles_list[i][1],alpha)
		third_point=get_point_in_segment(source_triangles_list[i][2],target_triangles_list[i][2],alpha)
		triangle=(first_point,second_point,third_point)
		new_triangles.append(triangle)
	return new_triangles




def get_array_of_matching_points(size,triangles_list ,
                                 intermediate_triangles_list):
	newlist=[[None]*size[1]]*size[0]
	for idx1 in range(0,size[1]):
		for idx2 in range(0,size[0]):
			point=(idx1,idx2)
			for idx3 in range(0,len(intermediate_triangles_list)):
				v1=intermediate_triangles_list[idx3][0]
				v2=intermediate_triangles_list[idx3][1]
				v3=intermediate_triangles_list[idx3][2]
				fitting_triangles=is_point_inside_triangle(point,v1,v2,v3)
				if fitting_triangles[0]:
					i=idx3
					a=fitting_triangles[1][0]
					b=fitting_triangles[1][1]
					c=fitting_triangles[1][2]
					v1=triangles_list[i][0]
					v2=triangles_list[i][1]
					v3=triangles_list[i][2]
					x=a*v1[0]+b*v2[0]+c*v3[0]
					y=a*v1[1]+b*v2[1]+c*v3[1]
					newlist[idx1][idx2]=(x,y)
	return (newlist)


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
	intermediate_triangles=get_intermediate_triangles(source_triangles_list, target_triangles_list, alpha)
	matching_source=get_array_of_matching_points(size,source_triangles_list,intermediate_triangles)
	matching_target=get_array_of_matching_points(size,target_triangles_list,intermediate_triangles)
	image=[[None]*size[1]]*size[0]
	for x in range(0,size[0]):
		for y in range(0,size[1]):
                        source_RGB=source_image[x,y]
                        target_RGB=target_image[x,y]
                        source_R=source_RGB[0]
                        source_G=source_RGB[1]
                        source_b=source_RGB[2]
                        target_R=target_RGB[0]
                        target_G=target_RGB[1]
                        target_b=target_RGB[2]
                        R=(1-alpha)*source_R+alpha*target_R
                        G=(1-alpha)*source_G+alpha*target_G
                        B=(1-alpha)*source_B+alpha*target_B
                        image[x][y]=(R,G,B)
	return image
			
	


def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):
	entire_seq=[]*num_frames
	for i in range(0,num_frames):
		alpha=i/(num_frames-1)
		entire_seq[i]=create_intermediate_image(alpha,size,source_image,target_image,source_triangles_list, target_triangles_list)
	return entire_seq



