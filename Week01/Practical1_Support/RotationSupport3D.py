import plotly.graph_objects as plt
import numpy as np
import pandas as pd

def transform3Daxes(tf, trans_enabled):
    x_axis = np.array([[1, 0, 0, 1]]).T
    y_axis = np.array([[0, 1, 0, 1]]).T
    z_axis = np.array([[0, 0, 1, 1]]).T
    origin = np.array([[0, 0, 0, 1]]).T
    if trans_enabled:
        x_axis_tf = tf @ x_axis
        y_axis_tf = tf @ y_axis
        z_axis_tf = tf @ z_axis
        origin_tf = tf @ origin
    else:
        x_axis_tf = tf @ x_axis[0:3]
        y_axis_tf = tf @ y_axis[0:3]
        z_axis_tf = tf @ z_axis[0:3]
        origin_tf = tf @ origin[0:3]

    xdata = np.array([origin_tf[0,0], x_axis_tf[0,0], origin_tf[0,0], y_axis_tf[0,0], origin_tf[0,0], z_axis_tf[0,0] ])
    ydata = np.array([origin_tf[1,0], x_axis_tf[1,0], origin_tf[1,0], y_axis_tf[1,0], origin_tf[1,0], z_axis_tf[1,0] ])
    zdata = np.array([origin_tf[2,0], x_axis_tf[2,0], origin_tf[2,0], y_axis_tf[2,0], origin_tf[2,0], z_axis_tf[2,0] ])

    return xdata, ydata, zdata

def plot3DRot(fig, xdata, ydata, zdata, title_txt):
    #fig = plt.Figure()
    #fig.data = []
    df_origin = pd.DataFrame(dict(
        X=[0,1,0,0,0,0],
        Y=[0,0,0,1,0,0],
        Z=[0,0,0,0,0,1]))

    fig.add_trace(
        plt.Scatter3d(
        x=df_origin.X, y=df_origin.Y, z=df_origin.Z,
        marker=dict(opacity=0.1, size=0.0001),
        line=dict(width=10, color='black',dash='dash')
        )
    )

    fig.add_trace(
        plt.Scatter3d(
        x=xdata[0:2], y=ydata[0:2], z=zdata[0:2],
        marker=dict(opacity=0.1, size=0.0001),
        line=dict(width=10, color='royalblue')
        )
    )

    fig.add_trace(
        plt.Scatter3d(
        x=xdata[2:4], y=ydata[2:4], z=zdata[2:4],
        marker=dict(opacity=0.1, size=0.0001),
        line=dict(width=10, color='red')
        )
    )

    fig.add_trace(
        plt.Scatter3d(
        x=xdata[4:], y=ydata[4:], z=zdata[4:],
        marker=dict(opacity=0.1, size=0.0001),
        line=dict(width=10, color='green')
        )
    )

    fig.update_layout(
        title=title_txt,
        scene = dict(
            xaxis = dict(nticks=12, range=[-3,3]),
                        yaxis = dict(nticks=12, range=[-3,3]),
                        zaxis = dict(nticks=12, range=[-3,3]),
                    ),
        autosize=False,
        width=700,
        height=700,
        scene_aspectmode='cube',
        showlegend=False
    )
    return fig
