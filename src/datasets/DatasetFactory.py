from datasets.Dataset import Dataset
from datasets.MBPPDataset import MBPPDataset,MBPPDataset_ET
from datasets.APPSDataset import APPSDataset
from datasets.XCodeDataset import XCodeDataset
from datasets.HumanEvalDataset import HumanDataset,HumanDatasetET
from datasets.CodeContestDataset import CodeContestDataset


class DatasetFactory:
    @staticmethod
    def get_dataset_class(dataset_name):
        if dataset_name == "APPS":
            return APPSDataset
        elif dataset_name == "MBPP":
            return MBPPDataset
        elif dataset_name == "MBPP_ET":
            return MBPPDataset_ET
        elif dataset_name == "xCodeEval":
            return XCodeDataset
        elif dataset_name == "HumanEval":
            return HumanDataset
        elif dataset_name == "HumanEval_ET":
            return HumanDatasetET
        elif dataset_name == "CC":
            return CodeContestDataset
        else:
            raise Exception(f"Unknown dataset name {dataset_name}")
