from matplotlib.patches import FancyArrowPatch
import matplotlib.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

class Rotation2D:

    def __init__(self):
        self.fig = plt.figure(figsize=(5, 5))
        self.fig.canvas.toolbar_position = 'top'
        self.axes = plt.gca()
        self.axes.set_xlim([-2.5,2.5])
        self.axes.set_ylim([-2.5,2.5])
        _ = self.axes.set_xticks(np.arange(-2.5, 2.5, 0.5))
        _ = self.axes.set_yticks(np.arange(-2.5, 2.5, 0.5))
        self.axes.tick_params(axis='both', which='major', labelsize=7)
        plt.title('Figure 1 - Overhead View')
        plt.xlabel('X (m)',weight='bold')
        plt.ylabel('Y (m)',weight='bold')

        self.world_ax = []
        self.world_ax.append(FancyArrowPatch((0,0), (0.5,0), mutation_scale=8,color='black'))
        self.world_ax.append(FancyArrowPatch((0,0), (0,0.5), mutation_scale=8,color='black'))

        self.robot_ax = []
        self.robot_ax.append(FancyArrowPatch((0,0), (0.6,0), mutation_scale=8,color='red'))
        self.robot_ax.append(FancyArrowPatch((0,0), (0,0.6), mutation_scale=8,color='green'))

        self.axes.add_patch(self.world_ax[0])
        self.axes.add_patch(self.world_ax[1])
        self.axes.add_patch(self.robot_ax[0])
        self.axes.add_patch(self.robot_ax[1])


        self.ax_trans = self.axes.transData


    def update_frame(self, new_transforms, figure, robot_ax, ax_trans):
        # transform is a dictionnary that contains a translation and a rotation change to apply to the frame
        # {'translation': np.array (2D), 'rotation': np.array (2x2 matrix)}
        figure.canvas.draw_idle()
        trans = new_transforms['translation'] if 'translation' in new_transforms else np.zeros(2)
        rot = new_transforms['rotation'] if 'rotation' in new_transforms else np.eye(2)
        Tw_r = np.eye(3)
        Tw_r[0:2,2] = trans
        Tw_r[0:2,0:2] = rot
        Tw_r_obj = transforms.Affine2D(Tw_r)
        robot_ax[0].set_transform(Tw_r_obj+ax_trans)
        robot_ax[1].set_transform(robot_ax[0].get_transform())
