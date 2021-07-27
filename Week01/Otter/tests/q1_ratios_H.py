test = {
	"name": "q1_ratios_H",
	"points": 3,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> r = np.round(get_homogeneous_transform_2d(1./2., 5, 5), 2)
					>>> answer = np.array([[ 0.,  -1.,  5.], [1.,  0.,  5.], [ 0.,  0.,  1.]])
					>>> np.all(np.isclose(r, answer)) 
					True
					""",
					"hidden": True,
					"locked": False,
				},
				{
					"code": r"""
					>>> r = np.round(get_homogeneous_transform_2d(-1./3., 0, -5), 2)
					>>> answer = np.array([[ 0.5,  0.87,  0.], [-0.87,  0.5,  -5.], [ 0.,  0.,  1.]])
					>>> np.all(np.isclose(r, answer)) 
					True
					""",
					"hidden": True,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> r = np.round(get_homogeneous_transform_2d(1, 1, 10), 2)
					>>> answer = np.array([[ -1.,  0.,  1.], [ 0.,  -1.,  10.], [ 0.,  0.,  1.]])
					>>> np.all(np.isclose(r, answer)) 
					True
					""",
					"hidden": True,
					"locked": False,
				} 
			],
			"scored": True,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}