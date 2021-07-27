test = {
	"name": "q2_ratios_world",
	"points": 2,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> r = np.round(get_point_in_world_frame(point_c=np.array([0, 1, 3]), gamma=0, disp_c=2, alpha=0, theta=0, disp_b=-1), 2).flatten()
					>>> answer = np.array([0., 0., 5.]).flatten()
					>>> np.all(np.isclose(r, answer))
					True
					""",
					"hidden": True,
					"locked": False,
				},
				{
					"code": r"""
					>>> r = np.round(get_point_in_world_frame(point_c=np.array([2, 0, 2]), gamma=0.5, disp_c=2, alpha=0.5, theta=0.25, disp_b=-1), 2).flatten()
					>>> answer = np.array([3.54, 2., 2.12]).flatten()
					>>> np.all(np.isclose(r, answer))
					True
					""",
					"hidden": True,
					"locked": False,
				},
				{
					"code": r"""
					>>> r = np.round(get_point_in_world_frame(point_c=np.array([1, 1, 1]), gamma=-1./3., disp_c=5, alpha=0.25, theta=1./3., disp_b=10), 2).flatten()
					>>> answer = np.array([-11.87, -1.72, 3.75]).flatten()
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
