import os
import yaml
import torch
import argparse

def get_useable_cuda(device_nums):
    test_tensor = torch.zeros((1))
    useable_cuda = []
    for i in range(device_num):
        try:
            test_tensor.to(device=i)
            useable_cuda.append(i)
        except:
            continue
    return useable_cuda

def main(args):

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    print("loading model.......")
    device = get_useable_cuda(torch.cuda.device_count())
    #model 就是简单getmodel，如果用deepspeed加载的话另说
    model = load_model().to(device)
    #load并处理datasets
    datasets = load_data()
    #主要功能集成在 evaluator类中，其中包括各种prompt，metric的处理方法等等,并自动进行结果保存
    evaluator = evaluator(model, datasets)
    evaluator.evaluate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluation")
    parser.add_argument("--model_cfg", type=str, required=True)
    parser.add_argument("--recipe_cfg", type=str, required=True)
    parser.add_argument("--save_dir", type=str, default="../results")
    parser.add_argument("--time", type=str, required=True)
    args = parser.parse_args()
    main(args)