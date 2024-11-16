require 'torch'
require 'image'
require 'paths'

local function loadAndSaveAsT7(inputDir, outputFile)
    local data = {}
    local labels = {}
    local classes = {'fall', 'spring', 'summer', 'winter'}

    for labelIndex, className in ipairs(classes) do
        local classPath = paths.concat(inputDir, className)
        for file in paths.files(classPath, function(f) return f:find('.png') end) do
            local filePath = paths.concat(classPath, file)
            local img = image.load(filePath, 3, 'float')
            if img then
                img = image.scale(img, 224, 224) -- 크기 조정
                table.insert(data, img)
                table.insert(labels, labelIndex)
            end
        end
    end

    local dataset = {
        data = torch.FloatTensor(data),
        labels = torch.LongTensor(labels)
    }

    torch.save(outputFile, dataset)
    print('Saved dataset to ' .. outputFile)
end

-- 변환 실행
local inputDir = './Datasets_png/personalColor/dataset/train'
local outputFile = './Datasets/personalColor/train_data.t7'
loadAndSaveAsT7(inputDir, outputFile)
