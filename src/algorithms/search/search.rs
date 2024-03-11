use crate::utils::{parser, structures::{BusinessInfo, FilterConditions, SortConditions}};

pub fn check_business(business_id: String) -> Option<BusinessInfo>{
    let path = "dataset/yelp_academic_dataset_business.json";
    let businesses : Vec<BusinessInfo> = parser::parse_json(path);
    for business in businesses {
        if business_id == business.business_id {
            return Some(business) 
        }
    }
    None
}

#[allow(unused)]
pub fn sort_business(sort_condition: SortConditions) {

}

#[allow(unused)]
pub fn filter_business(filter_condition: FilterConditions) {

}