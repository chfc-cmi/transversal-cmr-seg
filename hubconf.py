dependencies = ['torch','fastai']
import torch
import os.path
import tempfile
import fastai.vision

# b0_transversal_5_5 is the name of entrypoint
def b0_transversal_5_5(**kwargs):
    """ # This docstring shows up in hub.help()
    Initial model trained on 138 transversal images via transfer learning on the base model chfc-cmi/cmr-seg-tl : cmr_seg_base
    """
    # Call the model, load pretrained weights
    url = "https://github.com/chfc-cmi/transversal-cmr-seg/releases/download/0.1.0/b0_transversal_5_5.pth"
    dst = torch.hub.get_dir() + '/chfc-cmi_transversal-cmr-seg_master/' + 'b0_transversal_5_5.pth'
    if not os.path.isfile(dst):
        torch.hub.download_url_to_file(url,dst,progress=True)
    model = fastai.vision.load_learner(path=tempfile.gettempdir(),file=dst,tfm_y=False)
    return model
