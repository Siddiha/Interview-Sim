export type InterviewQuestion = {
    id: string;
    question: string;
    answer: string;
    category: string;
};

export type UserProfile = {
    name: string;
    email: string;
    experienceLevel: 'junior' | 'mid' | 'senior';
};

export type Category = {
    id: string;
    name: string;
};