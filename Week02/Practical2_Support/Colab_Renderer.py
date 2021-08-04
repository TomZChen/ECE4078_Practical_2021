import plotly.graph_objects as plt
from IPython.display import clear_output
import numpy as np

def plot_traj(robot_traj, title_txt):
    robot_traj = np.asarray(robot_traj)
    robot_traj = np.reshape(robot_traj, (-1,2))

    print('Please reset.')
    fig = plt.Figure()
    fig.add_trace(plt.Scatter(x=robot_traj[:,0], y=robot_traj[:,1],
              mode='markers+lines', name='Trajectory'))
    fig.add_trace(plt.Scatter(x=[robot_traj[0,0]], y=[robot_traj[0,1]],
              mode='markers', name='Initial'))
    fig.add_trace(plt.Scatter(x=[robot_traj[-1,0]], y=[robot_traj[-1,1]],
              mode='markers', name='Final'))
    fig.update_layout(
        title=title_txt,
        scene = dict(
                    xaxis = dict(nticks=12, range=[-4,1.5]),
                    yaxis = dict(nticks=12, range=[-3.5,1.5])
                ),
      autosize=False,
      width=700,
      height=700,
      showlegend=True,
      xaxis=dict(
        title="X (m)"
      ),
      yaxis=dict(
        title="Y (m)"
      )
    )
    fig.show()