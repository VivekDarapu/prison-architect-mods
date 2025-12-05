-- VivekGym Equipment Management Script
-- Manages fitness equipment effectiveness and prisoner health benefits

local equipment_stats = {
    Treadmill = { intensity = 7, health_gain = 2 },
    WeightBench = { intensity = 8, health_gain = 3 },
    YogaMat = { intensity = 3, health_gain = 1 },
    ResistanceBike = { intensity = 6, health_gain = 2.5 }
}

function startEquipmentSession(prisoner, equipment_name)
    local stats = equipment_stats[equipment_name]
    if not stats then return end
    
    local current_fitness = prisoner:getFitness() or 0
    local mood_increase = stats.intensity * 0.5
    prisoner:setMood(prisoner:getMood() + mood_increase)
    
    return {
        equipment = equipment_name,
        intensity = stats.intensity,
        time_required = 30
    }
end

function completeEquipmentSession(prisoner, equipment_name, duration)
    local stats = equipment_stats[equipment_name]
    if not stats then return end
    
    local health_improvement = (duration / 30) * stats.health_gain
    local current_health = prisoner:getHealth() or 50
    prisoner:setHealth(math.min(100, current_health + health_improvement))
    
    return health_improvement
end

function getGymEfficiency(equipment_list, prisoners)
    local total_efficiency = 0
    for _, eq in ipairs(equipment_list) do
        local stats = equipment_stats[eq] or { intensity = 5 }
        total_efficiency = total_efficiency + stats.intensity
    end
    return total_efficiency / #equipment_list
end
